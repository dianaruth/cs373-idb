/* Controllers */
angular.module('controllers', [])
    .controller('PeopleController', ['$scope' , function($scope) {

    }])
    .controller('PlanetsController', ['$scope' , function($scope) {

    }])
    .controller('SpeciesController', ['$scope' , function($scope) {

    }])
    .controller('AboutController', ['$scope' , function($scope) {
        $scope.teamMembers = [
            {"name": "Diana Ruth"},
            {"name": "Clint Ascencio"},
            {"name": "Tony Serino"},
            {"name": "Jamie Barbosa"},
            {"name": "Jon Lim"}
        ];
    }])
    .controller('NavController', ['$scope', '$location' , function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return $location.path().indexOf(viewLocation) == 0;
        }
    }]);
