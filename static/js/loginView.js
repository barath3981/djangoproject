
var CRMApp = angular.module('mainCRMApp.loginView', []);

CRMApp.controller('loginViewCtrl', ['$scope', '$rootScope', '$http',

    function($scope, $rootScope, $http){

        $rootScope.shredData1 = 'Shared success';

        $scope.signInPanelColor = '#2EFEF7';

        //console.log($rootScope.shredData1);

        $scope.loginObject = {

            userName: 'barathbaisetty@inviter.com',

            password: 'jaisriram'

        };

        $scope.loginError = false;

        $scope.loginErrorMessage = '';



        /*
        This method is used to send request for login
        */
        $scope.crmLoginRequest = function(loginObj){

            $scope.loginError = false;

            console.log(loginObj);

            $http({

              method: 'POST',

              url: 'login/',

              data:  'emailID='+loginObj.userName+'&password='+encodeURIComponent(loginObj.password),

              headers: {

                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

              }

            }).then(function successCallback(response) {

                if(response.data.status == 'success'){

                    getUserData($scope.loginObject.userName)

                }



              }, function errorCallback(response) {

                    $scope.loginError = true;

                    $scope.loginErrorMessage = response.data.message;

              });

        };






        /*
        * This method is used to get used data
        * */
        function getUserData(email){

            $http({

                method: 'POST',

                url: 'userdata/',

                data:  'emailID='+email,

                headers: {

                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

                }

            }).then(function successCallback(response) {

                console.log(response);

                if(response.data.status == 'success'){

                    console.log('User data: ', response);

                    $rootScope.userID = response.data.data.userid;

                    sessionStorage.setItem('userID', response.data.data.userid);

                    $rootScope.userEmail = response.data.data.email;

                    sessionStorage.setItem('email', response.data.data.email);

                    $rootScope.accessToken = response.data.data.accessToken;

                    sessionStorage.setItem('accessToken', response.data.data.accessToken);

                    $rootScope.appID = response.data.data.appID;

                    sessionStorage.setItem('appID', response.data.data.appID);

                    $rootScope.appSecret = response.data.data.appSecret;

                    sessionStorage.setItem('appSecret', response.data.data.appSecret);

                    document.location.href = '/dashboard';

                }

            }, function errorCallback(response) {

                if(response.data.status == 'error'){

                    alert('Error');

                }

            });

        }





        /*
        This method is used convert object to request data
        */
        $scope.objectToRequestData = function(dataObj){

            var form_data = '';

            for ( var key in dataObj ) {

                form_data = form_data+key+'='+dataObj[key]+'&';

            }

            return form_data.slice(0, -1);

        }

    }]);


CRMApp.config(function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});