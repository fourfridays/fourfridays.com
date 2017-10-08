module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['node_modules/jquery/dist/jquery.slim.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/transition.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/collapse.js', 'src/fourfridays.js'],
                dest: 'dist/js/fourfridays.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                compress: {},
                beautify: true
        },
        dist: {
            files: {
                '/home/fourfridays/sites/fourfridays/static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
                //'../static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '/home/fourfridays/sites/fourfridays/static/css/fourfridays.css': 'src/fourfridays.scss'
          //'../static/css/fourfridays.css': 'src/fourfridays.scss'
        }
      }
    },
    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: '/home/fourfridays/sites/fourfridays/static/css',
          src: ['*.css', '!*.min.css'],
          dest: '/home/fourfridays/sites/fourfridays/static/css',
          ext: '.min.css'
        }]
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass', 'cssmin'],
        // tasks: ['sass'],
        options: {
          livereload: true
        },
      },
    }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'cssmin', 'watch']);
    // grunt.registerTask('default', ['sass', 'watch']);

};
