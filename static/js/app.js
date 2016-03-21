/* Main Application */

var returnOfTheAPI = angular.module('returnOfTheAPI', ['controllers', 'ngRoute']);

returnOfTheAPI.config(['$routeProvider',
    function($routeProvider){
        $routeProvider.
            when('/', {
                templateUrl : '../static/partials/home.html',
                controller : 'HomeController'
            }).
            when('/about', {
                templateUrl : '../static/partials/about.html',
                controller : 'AboutController'
            }).
//            when('/albums', {
//                templateUrl : '/partials/albums.html',
//                controller : 'AlbumTableCtrl',
//                css : 'css/albums.css'
//            }).
//            when('/tracks', {
//                templateUrl : '/partials/tracks.html',
//                controller : 'TrackTableCtrl',
//                css : 'css/tracks.css'
//            }).
//            when('/test/:artistID', {
//                templateUrl : '/partials/artist-details.html',
//                controller : 'ArtistDetailsCtrl'
//            }).
//            when('/about', {
//                templateUrl : 'partials/about.html',
//                controller : 'AboutCtrl',
//                css : 'css/about.css'
//            }).
            otherwise({
                redirectTo: '/'
            });
}]);