/* Main Application */

var returnOfTheAPI = angular.module('returnOfTheAPI', ['controllers', 'ngRoute']);

returnOfTheAPI.config(['$routeProvider',
    function($routeProvider){
        $routeProvider.
            when('/', {
                templateUrl : '../static/partials/home.html',
                controller : 'HomeController'
            }).
            when('/about', {
                templateUrl : '../static/partials/about.html',
                controller : 'AboutController'
            }).
            otherwise({
                redirectTo: '/'
            });
}]);