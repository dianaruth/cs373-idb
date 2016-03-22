'use strict';

/* App Module */

var returnOfTheAPIApp = angular.module('returnOfTheAPIApp', [
    'ngRoute',
    'returnOfTheAPIAnimations',
    'returnOfTheAPIControllers',
    'returnOfTheAPIFilters',
    'returnOfTheAPIServices'
]);

returnOfTheAPIApp.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider){
        $routeProvider.
            when('/', {
                templateUrl : 'partials/home.html'
            }).
            when('/people', {
                templateUrl : 'partials/people.html',
                controller : 'PeopleListController'
            }).
            when('/planets', {
                templateUrl : 'partials/planets.html',
                controller : 'PlanetsListController'
            }).
            when('/species', {
                templateUrl : 'partials/species.html',
                controller : 'SpeciesListController'
            }).
            when('/about', {
                templateUrl : 'partials/about.html',
                controller : 'AboutController'
            }).
            when('/people/:personID', {
                templateUrl: 'partials/person-detail.html',
                controller: 'PersonDetailCtrl'
            }).
            when('/planets/:planetID', {
                templateUrl: 'partials/planet-detail.html',
                controller: 'PlanetDetailCtrl'
            }).
            when('/species/:speciesID', {
                templateUrl: 'partials/species-detail.html',
                controller: 'SpeciesDetailCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode({
            enabled: true
        });
}]);