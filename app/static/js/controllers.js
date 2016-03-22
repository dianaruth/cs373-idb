'use strict';

/* Controllers */

var returnOfTheAPIControllers = angular.module('returnOfTheAPIControllers', []);

returnOfTheAPIControllers.controller('PeopleListController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('PlanetsListController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('SpeciesListController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('PersonDetailController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('PlanetDetailController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('SpeciesDetailController', ['$scope',
    function($scope) {
        
    }]);

returnOfTheAPIControllers.controller('AboutController', ['$scope',
    function($scope) {
        $scope.teamMembers = [
            {"name": "Diana Ruth"},
            {"name": "Clint Ascencio"},
            {"name": "Tony Serino"},
            {"name": "Jamie Barbosa"},
            {"name": "Jon Lim"}
        ];
    }]);

returnOfTheAPIControllers.controller('NavController', ['$scope', '$location',
    function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
