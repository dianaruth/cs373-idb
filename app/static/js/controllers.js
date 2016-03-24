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

returnOfTheAPIControllers.controller('PersonDetailController', ['$scope', '$routeParams', 'peopleService',
    function($scope, $routeParams, peopleService) {
        var id = parseInt($routeParams.personID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "luke_skywalker.jpg";
                break;
            case 2:
                $scope.img = "c3po.png";
                break;
            case 3:
                $scope.img = "r2d2.png";
                break;
            default:
                break;
        }
        peopleService.getPeople().then(function(data) {
            $scope.person = data["people"][id - 1];
        });
    }]);

returnOfTheAPIControllers.controller('PlanetDetailController', ['$scope', '$routeParams', 'planetsService',
    function($scope, $routeParams, planetsService) {
        var id = parseInt($routeParams.planetID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "tattooine.png";
                break;
            case 2:
                $scope.img = "alderaan.jpg";
                break;
            case 3:
                $scope.img = "yavin4.jpg";
                break;
            default:
                break;
        }
        planetsService.getPlanets().then(function(data) {
            $scope.planet = data["planets"][id - 1];
        });
    }]);

returnOfTheAPIControllers.controller('SpeciesDetailController', ['$scope', '$routeParams', 'speciesService',
    function($scope, $routeParams, speciesService) {
        var id = parseInt($routeParams.speciesID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "human.jpg";
                break;
            case 2:
                $scope.img = "droid.jpg";
                break;
            case 3:
                $scope.img = "wookiee.jpg";
                break;
            default:
                break;
        }
        speciesService.getSpecies().then(function(data) {
            $scope.species = data["species"][id - 1];
        });
    }]);

returnOfTheAPIControllers.controller('AboutController', ['$scope',
    function($scope) {
        $scope.members = [
            {
                "name": "Diana Ruth",
                "photo": "diana.jpg",
                "bio": "Fourth year student studying electrical engineering and computer science. Loves web development and horses. Getting ready to spend a semester down under in Melbourne, Australia.",
                "responsibilities": ["Front-end development with AngularJS", "UI Design"], 
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Clint Ascencio",
                "photo": "clint.jpg",
                "bio": "First place in 'Most Likely to Appear in a Broccoli Commercial'", 
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker"],
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Tony Serino",
                "photo": "tony.jpg",
                "bio": "Computer Science student from Austin. Hobbies are video games and martial arts. 4x collegiate state judo champion. After graduation I will working as a software developer at Spiceworks.",
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker"],
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Jamie Barbosa",
                "photo": "jamie.jpg",
                "bio": "Senior CS student from Schertz, Tx. Loves travel and adventure. Hoping to move to NYC after graduation. Puppies are the best animals.",
                "responsibilities": ["UML Design", "Wiki"],
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Jon Lim",
                "photo": "jon.jpg",
                "bio": "A computer science student originally from Seoul, South Korea. Interests include bodybuilding and Texas hold'em. Once quadrupled his money playing poker for 15 minutes... then lost it all the next day.",
                "responsibilities": ["UML Design", "Wiki"],
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            }
        ];
    }]);

returnOfTheAPIControllers.controller('NavController', ['$scope', '$location',
    function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
