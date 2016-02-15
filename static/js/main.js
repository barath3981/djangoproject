require.config({
    //By default load any module IDs from js/lib
    catchError: true,
    baseUrl: '/static/js',

    paths: {

    },

    waitSeconds: 7000

});
// Start the main app logic.
require(['/static/sourceMin/cust.all.min.js'],function(){
    console.log('Loaded lib files');
    require(['/static/sourceMin/all.min.js'],function(){
        console.log("Loading app...");
        angular.bootstrap(document.body, [
            'mainCRMApp'
        ]);
        console.log('Loaded source files');
    });
});


require.onError = function (err) {
    if (err.requireType == 'timeout' || err.requireType =='scripterror') {
        //window.location.reload();
        alert('An error occurred please refresh the page');
        throw err;
    } else {
        //window.location.reload();
        alert('An error occurred please refresh the page!');
        //window.location.reload();
        throw err;
    }
};