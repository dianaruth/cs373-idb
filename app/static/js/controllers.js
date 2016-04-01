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

returnOfTheAPIControllers.controller('PersonDetailController', ['$scope', '$routeParams', 'personDetailService',
    function($scope, $routeParams, personDetailService) {
        var id = parseInt($routeParams.personID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "luke_skywalker.jpg";
                $scope.homeworld = "Tatooine";
                $scope.species = "Human";
                break;
            case 2:
                $scope.img = "c3po.png";
                $scope.homeworld = "Tatooine";
                $scope.species = "Droid";
                break;
            case 3:
                $scope.img = "r2d2.png";
                $scope.homeworld = "";
                $scope.species = "Droid";
                break;
            default:
                break;
        }
        personDetailService.getPerson(id).then(function(data) {
            $scope.person = data["person"];
        });
    }]);

returnOfTheAPIControllers.controller('PlanetDetailController', ['$scope', '$routeParams', 'planetDetailService',
    function($scope, $routeParams, planetDetailService) {
        var id = parseInt($routeParams.planetID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "tattooine.png";
                $scope.residents = ["Luke Skywalker", "C-3PO"];
                break;
            case 2:
                $scope.img = "alderaan.jpg";
                $scope.residents = [];
                break;
            case 3:
                $scope.img = "yavin4.jpg";
                $scope.residents = [];
                break;
            default:
                break;
        }
        planetDetailService.getPlanet(id).then(function(data) {
            $scope.planet = data["planet"];
        });
    }]);

returnOfTheAPIControllers.controller('SpeciesDetailController', ['$scope', '$routeParams', 'speciesDetailService',
    function($scope, $routeParams, speciesDetailService) {
        var id = parseInt($routeParams.speciesID);
        $scope.id = id;
        switch(id) {
            case 1:
                $scope.img = "human.jpg";
                $scope.homeworld = "";
                $scope.people = ["Luke Skywalker"];
                break;
            case 2:
                $scope.img = "droid.jpg";
                $scope.homeworld = "";
                $scope.people = ["C-3P0", "R2-D2"];
                break;
            case 3:
                $scope.img = "wookiee.jpg";
                $scope.homeworld = "";
                $scope.people = [];
                break;
            default:
                break;
        }
        speciesDetailService.getSpecies(id).then(function(data) {
            $scope.species = data["species"];
        });
    }]);

returnOfTheAPIControllers.controller('AboutController', ['$scope',
    function($scope) {
        $scope.members = [
            {
                "name": "Diana Ruth",
                "photo": "diana.jpg",
                "bio": "Fourth year student studying electrical engineering and computer science. Loves web development and horses. Getting ready to spend a semester down under in Melbourne, Australia. Thank god I'm not graduating yet.",
                "responsibilities": ["Front-end development with AngularJS", "UI Design", "External API data compilation", "Apiary API"], 
                "commits": 37,
                "issues": 17,
                "unit_tests": 0
            },
            {
                "name": "Clint Ascencio",
                "photo": "clint.jpg",
                "bio": "#3 in Forbe’s 'Top 20 Teen Fashion Writers Gone Tech Journalist' in 2018. Leading thought leader™ of the millennials. Avid fan of Hamilton-themed SoulCycle and Avocado Toast with pink himalayan salt. Accounting and computer science major. Year long software engineer intern and, after graduation, full-time employee at DataStax.", 
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker"],
                "commits": 26,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Tony Serino",
                "photo": "tony.jpg",
                "bio": "Computer Science student from Austin. Hobbies are video games and martial arts. 4x collegiate state judo champion. After graduation I will working as a software developer at Spiceworks.",
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker"],
                "commits": 18,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Jamie Barbosa",
                "photo": "jamie.jpg",
                "bio": "Senior CS student from Schertz, Tx. Loves travel and adventure. Hoping to move to NYC after graduation. Puppies are the best animals.",
                "responsibilities": ["UML Design", "GitHub Wiki"],
                "commits": 0,
                "issues": 0,
                "unit_tests": 0
            },
            {
                "name": "Jon Lim",
                "photo": "jon.jpg",
                "bio": "A computer science student originally from Seoul, South Korea. Interests include bodybuilding and Texas hold'em. Once quadrupled his money playing poker for 15 minutes... then lost it all the next day.",
                "responsibilities": ["GitHub Wiki", "Unit Testing", "Docker Setup"],
                "commits": 3,
                "issues": 1,
                "unit_tests": 9
            }
        ];
        $scope.teamStats = {
            "commits": 85,
            "issues": 18,
            "unit_tests": 9
        };
    }]);

returnOfTheAPIControllers.controller('NavController', ['$scope', '$location',
    function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
