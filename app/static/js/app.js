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
                templateUrl : 'partials/people.html'
            }).
            when('/planets', {
                templateUrl : 'partials/planets.html'
            }).
            when('/species', {
                templateUrl : 'partials/species.html'
            }).
            when('/about', {
                templateUrl : 'partials/about.html'
            }).
            when('/results', {
                templateUrl: 'partials/results.html'
            }).
            when('/people/:personID', {
                templateUrl: 'partials/person-detail.html'
            }).
            when('/planets/:planetID', {
                templateUrl: 'partials/planet-detail.html'
            }).
            when('/species/:speciesID', {
                templateUrl: 'partials/species-detail.html'
            }).
            otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode({
            enabled: true
        });
}]);