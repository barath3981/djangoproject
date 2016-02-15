(function(angular){
    'use strict';

    var CRMApp = angular.module('mainCRMApp', ['ngRoute',
                                                'ui.router',
                                                'mainCRMApp.dahsboardView',
                                                'mainCRMApp.loginView']);

    CRMApp.controller('mainCRMCtrl', function($rootScope){

        $rootScope.userID = '';
        $rootScope.userEmail = '';
        $rootScope.accessToken = '';
        $rootScope.appID = '';
        $rootScope.appSecret = '';

    });

    })(angular);

