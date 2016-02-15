(function(angular){
    'use strict';
var CRMApp = angular.module('mainCRMApp.dahsboardView', []);

    if(CRMApp.register != undefined){
        CRMApp = CRMApp.register;
    }

    CRMApp.controller('dashboardViewCtrl', ['$scope', '$rootScope', '$http' ,

        function($scope, $rootScope, $http){

            $scope.allEvents = '';

            if(sessionStorage.getItem('email') == null){

                //document.location.href = '/';

            }

            $http({

                method: 'POST',

                url: '/getevents/',

                headers: {

                    "accessToken": sessionStorage.getItem('accessToken'),

                    "appID": sessionStorage.getItem('appID'),

                    "appSecret": sessionStorage.getItem('appSecret')

                }

            }).then(function successCallback(response) {

                console.log(response);

                if(response.data.status == 'success'){

                    console.log('All events: ', response);

                    $scope.allEvents = response.data.data;

                    //document.location.href = '/dashboard';

                }

            }, function errorCallback(response) {

                if(response.data.status == 'error'){



                }

            });





            /*
            * This method is used to logout the session
            * */
            $scope.logout = function(){

                $http({

                    method: 'POST',

                    url: '/logout/',

                    headers: {

                        "accessToken": sessionStorage.getItem('accessToken'),

                        "appID": sessionStorage.getItem('appID'),

                        "appSecret": sessionStorage.getItem('appSecret')

                    }

                }).then(function successCallback(response) {

                    console.log('Response: ',response);

                    if(response.data.status == 'success'){

                        document.location.href = '/';

                    }

                }, function errorCallback(response) {

                });

            };






            /**
             *  VIEW MAPPING Function
             */
            $scope.eventStatusToText = function(flag)
            {

                if(flag == 'DR'){$scope.labelClassStatus = 'label label-default'; return 'Draft';}

                if(flag == 'SS'){$scope.labelClassStatus = 'label label-success'; return 'Sent';}

                if(flag == 'SB'){$scope.labelClassStatus = 'label label-warning'; return 'Submitted';}

                if(flag == 'SH'){$scope.labelClassStatus = 'label label-primary'; return 'Scheduled';}

                if(flag == 'CC'){$scope.labelClassStatus = 'label label-danger'; return 'Canceled';}

                if(flag == 'XX'){$scope.labelClassStatus = 'label label-danger'; return 'Deleted';}

                if(flag == 'ST'){$scope.labelClassStatus = 'label label-warning'; return 'Staging';}

                if(flag == 'PB'){$scope.labelClassStatus = 'label label-info'; return 'Public';}

                if(flag == ""){$scope.labelClassStatus = 'label label-default'; return "";}

                if(flag != 'DR' || flag != 'SS' || flag != 'SB' || flag != 'SH' || flag != 'CC' || flag != 'XX' || flag != 'ST' || flag != 'PB' || flag != ''){

                    console.log("Some error data receive into eventStatusToText method.");

                    return "unknown data received";

                }

            };



        }]);

})(angular);



/*
dashboardApp.controller('dashboardViewCtrl', function($scope, $rootScope, $http){



    */
/*
    This is for sending request for get events
    *//*

    */
/*$http({

          method: 'POST',

          url: 'getEvents/',

          data:  'emailID=barathbaisetty@inviter.com',



        }).then(function successCallback(response) {

            console.log(response);

            if(response.data.status == 'success'){

                document.location.href = '/dashboard';

            }



          }, function errorCallback(response) {

            if(response.data.status == 'error'){

                $scope.loginError = true;

                $scope.loginErrorMessage = response.data.message;

            }

          });*//*


});*/
