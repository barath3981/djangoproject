module.exports = function(grunt) {
    grunt.initConfig({ pkg: grunt.file.readJSON('package.json'),
    uglify: {
            options: {
                mangle: false,/*{
                 except: ['jQuery', 'angular', 'exceptionLogService', 'printStackTrace']
                 },*/
                compress: {
                    drop_console: false  // <-
                }
            },
            production: {
                files: {
                    //'public/js/app/services.min.js': ['public/js/app/services/*.js'],
                    'static/sourceMin/all.min.js': [
                        'static/js/app.js',
                        //'static/js/routes.js',
                        'static/js/loginView.js',
                        'static/js/dashboardView.js'

                    ],

                    'static/sourceMin/cust.all.min.js': [
                        'static/js/lib/jquery/jquery.min.js',
                        'static/bootstrap-3.3.6-dist/js/bootstrap.min.js',
                        'static/js/lib/Angular/angularNew.js',
                        'static/js/lib/Angular/angular-route.min.js',
                        'static/js/lib/Angular/angular-ui-router.min.js'
                    ]

                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-contrib-less");
    grunt.loadNpmTasks('grunt-contrib-compress');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-requirejs');

    grunt.registerTask("minify", ["uglify"]);

};