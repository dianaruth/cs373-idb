/* Code to hide intro text */
$("#continue").click(function() {
    $("#intro").fadeOut(1000, function() {
        $("#content").fadeIn(2000);
    });
});

/* Angular */
angular.module('returnOfTheAPI', ['ngRoute'])

.controller('MainController', function($scope, $route, $routeParams, $location) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
})

.controller('NavController', function($scope, $location) {
    $scope.isActive = function(viewLocation) {
        return $location.path().indexOf(viewLocation) == 0;
    }
})

.controller('HomeController', function($scope, $routeParams) {
    $scope.name = "HomeController";
    $scope.params = $routeParams;
})

//.controller('ChapterController', function($scope, $routeParams) {
//    $scope.name = "ChapterController";
//    $scope.params = $routeParams;
//})

.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('../partials/home', {
            templateUrl: 'home.html',
            controller: 'HomeController'
//            resolve: {
//                // I will cause a 1 second delay
//                delay: function($q, $timeout) {
//                    var delay = $q.defer();
//                    $timeout(delay.resolve, 1000);
//                    return delay.promise;
//                }
//            }
        })
        .when('/Book/:bookId/ch/:chapterId', {
            templateUrl: 'chapter.html',
            controller: 'ChapterController'
        });
});