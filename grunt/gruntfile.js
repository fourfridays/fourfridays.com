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
                '/mnt/volume-nyc1-01-part2/static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
                //'../static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '/mnt/volume-nyc1-01-part2/static/css/fourfridays.css': 'src/fourfridays.scss'
          //'../static/css/fourfridays.css': 'src/fourfridays.scss'
        }
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass'],
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
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'watch']);
    // grunt.registerTask('default', ['sass', 'watch']);

};
