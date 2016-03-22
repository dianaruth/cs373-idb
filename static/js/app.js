var returnOfTheAPI = angular.module('returnOfTheAPI', ['controllers', 'ngRoute']);

returnOfTheAPI.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider){
        $routeProvider.
            when('/', {
                templateUrl : 'static/partials/home.html'
            }).
            when('/people', {
                templateUrl : 'static/partials/people.html',
                controller : 'PeopleController'
            }).
            when('/planets', {
                templateUrl : 'static/partials/planets.html',
                controller : 'PlanetsController'
            }).
            when('/species', {
                templateUrl : 'static/partials/species.html',
                controller : 'SpeciesController'
            }).
            when('/about', {
                templateUrl : 'static/partials/about.html',
                controller : 'AboutController'
            }).
            otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode({
            enabled: true
        });
}]);