/* Controllers */
angular.module('controllers', [])
    .controller('HomeController',['$scope', function($scope) {
    
    }])
    .controller('AboutController', ['$scope' , function($scope) {

    }])
    .controller('NavController', ['$scope', '$location' , function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
