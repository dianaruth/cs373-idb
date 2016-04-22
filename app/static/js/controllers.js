'use strict';

/* Controllers */

var returnOfTheAPIControllers = angular.module('returnOfTheAPIControllers', []);

returnOfTheAPIControllers.controller('PeopleListController', ['$scope', 'peopleService',
    function($scope, peopleService) {
        $scope.people = [];
        peopleService.getPeople().then(function(data) {
            $scope.people = data.people;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
            $scope.currentPage = 1;
            $scope.pageSize = 10;
        });
    }]);

returnOfTheAPIControllers.controller('PlanetsListController', ['$scope', 'planetsService',
    function($scope, planetsService) {
        $scope.planets = [];
        planetsService.getPlanets().then(function(data) {
            $scope.planets = data.planets;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
            $scope.currentPage = 1;
            $scope.pageSize = 10;
        });
    }]);

returnOfTheAPIControllers.controller('SpeciesListController', ['$scope', 'speciesService',
    function($scope, speciesService) {
        $scope.species = [];
        speciesService.getSpecies().then(function(data) {
            $scope.species = data.species;
            $scope.sortType = 'name';
            $scope.sortReverse = false;
            $scope.currentPage = 1;
            $scope.pageSize = 10;
        });
    }]);

returnOfTheAPIControllers.controller('PersonDetailController', ['$scope', '$routeParams', 'personDetailService', 'planetForPersonService', 'speciesForPersonService',
    function($scope, $routeParams, personDetailService, planetForPersonService, speciesForPersonService) {
        var id = parseInt($routeParams.personID);
        $scope.id = id;
        personDetailService.getPerson(id).then(function(data) {
            $scope.person = data["person"];
        });
        planetForPersonService.getPlanetForPerson(id).then(function(data) {
            $scope.homeworld = data["homeworld"];
        });
        speciesForPersonService.getSpeciesForPerson(id).then(function(data) {
            $scope.species = data["species"];
        });
    }]);

returnOfTheAPIControllers.controller('PlanetDetailController', ['$scope', '$routeParams', 'planetDetailService', 'peopleForPlanetService', 'speciesForPlanetService',
    function($scope, $routeParams, planetDetailService, peopleForPlanetService, speciesForPlanetService) {
        var id = parseInt($routeParams.planetID);
        $scope.id = id;
        planetDetailService.getPlanet(id).then(function(data) {
            $scope.planet = data["planet"];
        });
        peopleForPlanetService.getPeopleForPlanet(id).then(function(data) {
            $scope.residents = data["residents"];
        });
        speciesForPlanetService.getSpeciesForPlanet(id).then(function(data) {
            $scope.native_species = data["native_species"];
        });
    }]);

returnOfTheAPIControllers.controller('SpeciesDetailController', ['$scope', '$routeParams', 'speciesDetailService', 'peopleForSpeciesService', 'planetForSpeciesService',
    function($scope, $routeParams, speciesDetailService, peopleForSpeciesService, planetForSpeciesService) {
        var id = parseInt($routeParams.speciesID);
        $scope.id = id;
        speciesDetailService.getSpecies(id).then(function(data) {
            $scope.species = data["species"];
        });
        peopleForSpeciesService.getPeopleForSpecies(id).then(function(data) {
            $scope.people = data["people"];
        });
        planetForSpeciesService.getPlanetForSpecies(id).then(function(data) {
            $scope.native_planet = data["native_planet"];
        });
    }]);

returnOfTheAPIControllers.controller('SearchController', ['$scope', '$location', '$route',
    function($scope, $location, $route) {
        $scope.search = function() {
            $route.reload();
            $location.path('/results');
        }
    }]);

returnOfTheAPIControllers.controller('SearchResultsController', ['$scope', '$sce', 'searchService',
    function($scope, $sce, searchService) {
        $scope.highlight = function(text, search) {
            var a = search.split(" ");
            var result = text;
            var pattern, original;
            for (var i = 0; i < a.length; i++) {
                pattern = new RegExp(a[i], 'gi');
                original = result.match(pattern);
                result = result.replace(pattern, '<span class="highlighted">' + original + '</span>');
            }
            return $sce.trustAsHtml(result.toString());
        };
        var query = $('#search-text').val();
        if (query != "") {
            $scope.loading = true;
            $scope.query = query;
            searchService.search(query).then(function(data) {
                $scope.and = data["AND"];
                $scope.or = data["OR"];
                $scope.loading = false;
            });
        }
    }]);

returnOfTheAPIControllers.controller('AboutController', ['$scope',
    function($scope) {
        $scope.members = [
            {
                "name": "Diana Ruth",
                "photo": "diana.jpg",
                "bio": "Fourth year student from Alpharetta, GA studying electrical engineering and computer science. Loves web development and horses. Getting ready to spend a semester down under in Melbourne, Australia.",
                "responsibilities": ["Frontend development with AngularJS", "UI Design", "Data Scraping", "Apiary API", "Frontend Search"], 
                "commits": 86,
                "issues": 23,
                "unit_tests": 5
            },
            {
                "name": "Clint Ascencio",
                "photo": "clint.jpg",
                "bio": "#3 in Forbe’s 'Top 20 Teen Fashion Writers Gone Tech Journalist' in 2018. Leading thought leader™ of the millennials. Avid fan of Hamilton-themed SoulCycle and Avocado Toast with pink himalayan salt. Accounting and computer science major. Year long software engineer intern and, after graduation, full-time employee at DataStax.", 
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker", "Database", "Backend Search"],
                "commits": 85,
                "issues": 3,
                "unit_tests": 3
            },
            {
                "name": "Tony Serino",
                "photo": "tony.jpg",
                "bio": "Originally from the wastelands of Siberia. My mother lost her life fighting ninjas and ebola at the same time when I was baby, and my other mother who's life choices you should respect sacrificed herself using love magic to protect me from the evil lord Voldermort. Hobbies mostly include survival and hiding from the CIA. They aren't looking for me, but if they ever start they're gonna be in for a hell of a surprise. I am the last surviving heir to house Stark and am currently working on my next iron man suit to kill king Justin Beiber for starting the war in Westoros. HAIL HYDRA!",
                "responsibilities": ["Created models", "Initialized Flask project", "Set up Docker", "Database", "Backend Search"],
                "commits": 32,
                "issues": 2,
                "unit_tests": 2
            },
            {
                "name": "Jamie Barbosa",
                "photo": "jamie.jpg",
                "bio": "Senior CS student from Schertz, TX. Loves travel and adventure. Hoping to move to NYC after graduation. Puppies are the best animals.",
                "responsibilities": ["UML Design", "GitHub Wiki", "Backend Search"],
                "commits": 8,
                "issues": 13,
                "unit_tests": 4
            },
            {
                "name": "Jon Lim",
                "photo": "jon.jpg",
                "bio": "A computer science student originally from Seoul, South Korea. Interests include bodybuilding and Texas hold'em. Once quadrupled his money playing poker for 15 minutes... then lost it all the next day.",
                "responsibilities": ["GitHub Wiki", "Unit Testing", "Docker Setup", "Database", "Backend Search"],
                "commits": 49,
                "issues": 9,
                "unit_tests": 38
            }
        ];
        $scope.teamStats = {
            "commits": 260,
            "issues": 50,
            "unit_tests": 52
        };
    }]);

returnOfTheAPIControllers.controller('RunTestsController', ['$scope', 'runTestsService',
    function($scope, runTestsService) {
        $scope.output = "Click the button above to run unit tests.";
        $scope.runTests = function() {
            $scope.output = "Running...";
            runTestsService.runTests().then(function(data) {
                $scope.output = data["output"];
            });
        }
    }]);

returnOfTheAPIControllers.controller('NavController', ['$scope', '$location',
    function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
