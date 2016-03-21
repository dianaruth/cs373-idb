var returnOfTheAPI = angular.module('returnOfTheAPI', ['controllers', 'ngRoute']);

returnOfTheAPI.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider){
        $routeProvider.
            when('/', {
                templateUrl : '/static/partials/home.html',
                controller : 'HomeController'
            }).
            when('/about', {
                templateUrl : '/static/partials/about.html',
                controller : 'AboutController'
            }).
            otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });
}]);