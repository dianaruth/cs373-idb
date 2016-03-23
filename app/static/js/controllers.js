'use strict';

/* Controllers */

var returnOfTheAPIControllers = angular.module('returnOfTheAPIControllers', []);

returnOfTheAPIControllers.controller('PeopleListController', ['$scope', 'peopleService',
    function($scope, peopleService) {
        $scope.people = []
        peopleService.getPeople().then(function(data) {
            $scope.people = data.people;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
        });
    }]);

returnOfTheAPIControllers.controller('PlanetsListController', ['$scope', 'planetsService',
    function($scope, planetsService) {
        $scope.planets = []
        planetsService.getPlanets().then(function(data) {
            $scope.planets = data.planets;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
        });
    }]);

returnOfTheAPIControllers.controller('SpeciesListController', ['$scope', 'speciesService',
    function($scope, speciesService) {
        $scope.species = []
        speciesService.getSpecies().then(function(data) {
            $scope.species = data.species;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
        });
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
