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