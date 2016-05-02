'use strict';

/* Services */

var returnOfTheAPIServices = angular.module('returnOfTheAPIServices', ['ngResource']);


returnOfTheAPIServices.factory('peopleService', function($http) {
    return {
        getPeople: function() {
            return $http.get('/get_people').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('planetsService', function($http) {
    return {
        getPlanets: function() {
            return $http.get('/get_planets').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('speciesService', function($http) {
    return {
        getSpecies: function() {
            return $http.get('/get_species').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('personDetailService', function($http) {
    return {
        getPerson: function(id) {
            return $http.get('/get_person/' + id).then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('planetDetailService', function($http) {
    return {
        getPlanet: function(id) {
            return $http.get('/get_planet/' + id).then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('speciesDetailService', function($http) {
    return {
        getSpecies: function(id) {
            return $http.get('/get_s/' + id).then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('planetForPersonService', function($http) {
    return {
        getPlanetForPerson: function(id) {
            return $http.get('/person/' + id + '/planet').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('speciesForPersonService', function($http) {
    return {
        getSpeciesForPerson: function(id) {
            return $http.get('/person/' + id + '/species').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('peopleForPlanetService', function($http) {
    return {
        getPeopleForPlanet: function(id) {
            return $http.get('/planet/' + id + '/people').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('speciesForPlanetService', function($http) {
    return {
        getSpeciesForPlanet: function(id) {
            return $http.get('/planet/' + id + '/species').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('peopleForSpeciesService', function($http) {
    return {
        getPeopleForSpecies: function(id) {
            return $http.get('/species/' + id + '/people').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('planetForSpeciesService', function($http) {
    return {
        getPlanetForSpecies: function(id) {
            return $http.get('/species/' + id + '/planet').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('searchService', function($http) {
    return {
        search: function(query) {
            return $http.get('/search/' + query).then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('runTestsService', function($http) {
    return {
        runTests: function() {
            return $http.get('/run_tests').then(function(r) {
                return r.data;
            });
        }
    }
});

returnOfTheAPIServices.factory('comproService', function($http) {
    return {
        getData: function() {
            return $http.get('/get_compro_data').then(function(r) {
                return r.data;
            });
        }
    }
});