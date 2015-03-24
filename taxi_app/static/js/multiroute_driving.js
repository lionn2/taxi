var myMap;  //голона карта
var trafficButton, viaPointButton;  //кнопки для побудови мартшруту з урахуванням пробок і ще якоїсь фігні
var multiRoute; //сам маршрут
var geolocation;    //об’єкт геолокації
var start, end;     //точки початку і кінця маршу
var route_data;      //результати вимірювань для маршруту

function way(start, end) {
    multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [ start, end ],
        params: {
            results: 5
        }
    }, {
        boundsAutoApply: true
    });
    myMap.geoObjects.removeAll();
    myMap.geoObjects.add(multiRoute);
    //var routes = multiRoute.getRoutes();
    //console.log(routes.length);
}

function add_controls_to_map(){
    if (myMap.controls.indexOf(trafficButton) == -1) {
        trafficButton = new ymaps.control.Button({
                data: { content: "Учитывать пробки" },
                options: { selectOnClick: true }
            }),
            viaPointButton = new ymaps.control.Button({
                data: { content: "Добавить транзитную точку" },
                options: { selectOnClick: true }
            });
        
        trafficButton.events.add('select', function () {
            multiRoute.model.setParams({ avoidTrafficJams: true }, true);
        });

        trafficButton.events.add('deselect', function () {
            multiRoute.model.setParams({ avoidTrafficJams: false }, true);
        });

        viaPointButton.events.add('select', function () {
            var referencePoints = multiRoute.model.getReferencePoints();
            referencePoints.splice(1, 0);
            multiRoute.model.setReferencePoints(referencePoints, [1]);
        });

        viaPointButton.events.add('deselect', function () {
            var referencePoints = multiRoute.model.getReferencePoints();
            referencePoints.splice(1, 1);
            multiRoute.model.setReferencePoints(referencePoints, []);
        });
        myMap.controls.add(trafficButton);
        myMap.controls.add(viaPointButton);
    }
}

function create_way_from_names_of_places(){
    start = document.getElementById('start').value;
    end = document.getElementById('end').value;
    way(start, end);
    route_length();
    add_controls_to_map();
    start = "";
    end = "";
}

function create_way_from_points(){
    if((typeof start[0] !== "undefined" && typeof end[0] !== "undefined") || (start == "" && end == "")) {
        way(start, end);
        data = route_length();
        delete start[0];
        delete end[0];
        add_controls_to_map();
    }
}

function return_data_route(){
    distance = document.getElementById("route_data_distance").innerHTML;
    duration = document.getElementById("route_data_duration").innerHTML;
    data = distance.split("&");
    data2 = data[1].split(";");
    distance = data[0]+data2[1];
    data = duration.split("&");
    data2 = data[1].split(";");
    duration = data[0]+data2[1];
    data = Data_route(distance, duration);
    $.getScript("server_post.js", post_route_data(data));
    return data;
}

function init () {
    geolocation = ymaps.geolocation;
    myMap = new ymaps.Map('map', {
        center: [55, 34],
        zoom: 10
    });

    // Сравним положение, вычисленное по ip пользователя и
    // положение, вычисленное средствами браузера.
    geolocation.get({
        provider: 'yandex',
        mapStateAutoApply: true
    }).then(function (result) {
        // Красным цветом пометим положение, вычисленное через ip.
        result.geoObjects.options.set('preset', 'islands#redCircleIcon');
        result.geoObjects.get(0).properties.set({
            balloonContentBody: 'Мое местоположение'
        });
        myMap.geoObjects.add(result.geoObjects);
    });

    geolocation.get({
        provider: 'browser',
        mapStateAutoApply: true
    }).then(function (result) {
        // Синим цветом пометим положение, полученное через браузер.
        // Если браузер не поддерживает эту функциональность, метка не будет добавлена на карту.
        result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
        myMap.geoObjects.add(result.geoObjects);
    });
}

function my_place(){
    pos = Array(2)
    geolocation.get({
        provider: 'browser',
        mapStateAutoApply: true
    }).then(function (result) {
        pos[0] = result.geoObjects.position[0];
        pos[1] = result.geoObjects.position[1];
    });
    return pos;
}

function createPoint(pos, text){
    setTimeout(function() {
        point1 = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: pos
            },
            properties: {
                iconContent: text,
                hintContent: 'Переставте на потрібну позицію'
                }
            }, {
                preset: 'islands#blackStretchyIcon',
                draggable: true
            });
            myMap.geoObjects.add(point1);
        }, 1000);
    return pos;
}

function click_on_map(){
    var pos = Array(2);
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');
        if ((typeof start === "undefined") || (start[0] == undefined) ) {
            start = Array(2);
            start[0] = coords[0].toPrecision(6);
            start[1] = coords[1].toPrecision(6);
            createPoint(start, "Початок");
        }
        else{
            end = Array(2);
            end[0] = coords[0].toPrecision(6);
            end[1] = coords[1].toPrecision(6);
            createPoint(end, "Кінець"); 
        }
    });
}


function Data_route(length, time) {
    this.length_route = length;
    this.time_route = time;
    return {"distance": this.length_route, "duration":this.time_route};

}


function route_length() {
    var multiRouteModel = new ymaps.multiRouter.MultiRouteModel([ start, end ], {
        boundsAutoApply: true
    });

    ymaps.modules.require([
            'MultiRouteCustomView'
        ], function (MultiRouteCustomView) {
            new MultiRouteCustomView(multiRouteModel);
    });

    ymaps.modules.define('MultiRouteCustomView', ['util.defineClass'], 
    route_res = function (provide, defineClass) {
    // Класс простого текстового отображения модели мультимаршрута.
    function CustomView (multiRouteModel) {
        this.multiRouteModel = multiRouteModel;
        // Объявляем начальное состояние.
        this.state = "init";
        this.stateChangeEvent = null;
        this.outputElement = $('<div></div>').appendTo('#viewContainer');

        this.rebuildOutput();
        multiRouteModel.events
            .add(["requestsuccess", "requestfail", "requestsend"], this.onModelStateChange, this);
    }

    // Таблица соответствия идентификатора состояния имени его обработчика.
    CustomView.stateProcessors = {
        init: "processInit",
        requestsend: "processRequestSend",
        requestsuccess: "processSuccessRequest",
        requestfail: "processFailRequest"
    };

    // Таблица соответствия типа маршрута имени его обработчика.
    CustomView.routeProcessors = {
        "driving": "processDrivingRoute",
        "masstransit": "processMasstransitRoute"
    };

    defineClass(CustomView, {
        // Обработчик событий модели.
        onModelStateChange: function (e) {
            // Запоминаем состояние модели и перестраиваем текстовое описание.
            this.state = e.get("type");
            this.stateChangeEvent = e;
            this.rebuildOutput();
    },

        rebuildOutput: function () {
            // Берем из таблицы обработчик для текущего состояния и исполняем его.
            var processorName = CustomView.stateProcessors[this.state];
            this.outputElement.html(
                this[processorName](this.multiRouteModel, this.stateChangeEvent)
            );
        },

        processInit: function () {
            return "Инициализация ...";
        },

        processRequestSend: function () {
            return "Запрос данных ...";
        },

        processSuccessRequest: function (multiRouteModel, e) {
            var routes = multiRouteModel.getRoutes(),
                result = ["Данные успешно получены."];
            if (routes.length) {
                result.push("Всего маршрутов: " + routes.length + ".");
                for (var i = 0, l = routes.length; i < l; i++) {
                    result.push(this.processRoute(i, routes[i]));
                }
            } else {
                result.push("Нет маршрутов.");
            }
            return result.join("<br/>");
        },

        processFailRequest: function (multiRouteModel, e) {
            return e.get("error").message;
        },

        processRoute: function (index, route) {
            // Берем из таблицы обработчик для данного типа маршрута и применяем его.
            var processorName = CustomView.routeProcessors[route.properties.get("type")];
            return (index + 1) + ". " + this[processorName](route);
        },

        processDrivingRoute: function (route) {
            var result = ["Автомобильный маршрут."];
            result.push(this.createCommonRouteOutput(route));
            return result.join("<br/>");
        },

        // Метод формирующий общую часть описания для обоих типов маршрутов.
        createCommonRouteOutput: function (route) {
            dis = route.properties.get("distance").text;
            dur = route.properties.get("duration").text;
            if (typeof route_data == "undefined")
                route_data = new Data_route(dis, dur);
            return "Протяженность маршрута: " + "<div id=\"route_data_distance\">" +route.properties.get("distance").text+ "</div>" + "<br/>" +
                "Время в пути: " + "<div id=\"route_data_duration\">" + route.properties.get("duration").text + "</div>";
        },

        destroy: function () {
            this.outputElement.remove();
            this.multiRouteModel.events
                .remove(["requestsuccess", "requestfail", "requestsend"], this.onModelStateChange, this);
        }
    });
    provide(CustomView);
})
}


ymaps.ready(init);
