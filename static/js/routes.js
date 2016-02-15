(function(angular){
    'use strict';

var CRMApp  = angular.module('mainCRMApp');

CRMApp.controller('mainCRMCtrl', function($rootScope){
//$rootScope.shredData1 = 'Shared success';
});
    CRMApp.config(function($routeProvider, $stateProvider, $locationProvider) {
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    }).hashPrefix('!');
    $routeProvider
        // route for the home page
        .when('/', {
            templateUrl : '/static/templates/loginView.html',
            controller  : 'loginViewCtrl'
        })
        // route for the about page
        .when('/dashboard', {
            templateUrl : '/static/templates/dashboardView.html',
            controller  : 'dashboardViewCtrl'
        });
    });

})(angular);

