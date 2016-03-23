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