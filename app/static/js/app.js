'use strict';

/* App Module */

var returnOfTheAPIApp = angular.module('returnOfTheAPIApp', [
    'ngRoute',
    'angularUtils.directives.dirPagination',
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
                controller: 'PersonDetailController'
            }).
            when('/planets/:planetID', {
                templateUrl: 'partials/planet-detail.html',
                controller: 'PlanetDetailController'
            }).
            when('/species/:speciesID', {
                templateUrl: 'partials/species-detail.html',
                controller: 'SpeciesDetailController'
            }).
            when('/search/:query', {
                templateUrl: 'partials/results.html',
                controller: 'SearchResultsController'
            }).
            otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode({
            enabled: true
        });
}]);