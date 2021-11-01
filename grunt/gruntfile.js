module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['node_modules/jquery/dist/jquery.slim.js', 'node_modules/bootstrap/js/dist/util.js', 'node_modules/bootstrap/js/dist/collapse.js', 'src/fourfridays.js'],
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
                '../static/js/fourfridays.min.js': ['<%= concat.dist.dest %>'],
                '../static/js/fontawesome-free.min.js': ['node_modules/@fortawesome/fontawesome-free/js/all.js'],
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
          ext: '.min.<%= grunt.template.today("yyyy-mm-dd") %>.css'
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