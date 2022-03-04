module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['node_modules/bootstrap/dist/js/bootstrap.bundle.js', 'src/fourfridays.js'],
                dest: 'dist/fourfridays.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                mangle: true,
                compress: true,
                beautify: false
        },
        dist: {
            files: {
                //'/home/fourfridays/sites/fourfridays/static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
                '../static/js/fourfridays.min.js': ['<%= concat.dist.dest %>']
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          //'/home/fourfridays/sites/fourfridays/static/css/fourfridays.css': 'src/fourfridays.scss'
          'dist/fourfridays.css': 'src/fourfridays.scss',
        }
      }
    },
    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: 'dist',
          src: ['*.css', '!*.min.css'],
          dest: '../static/css',
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