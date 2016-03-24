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