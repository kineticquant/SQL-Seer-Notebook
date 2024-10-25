var editor = ace.edit("editor");
        
        editor.session.setMode("ace/mode/sql");
        editor.setTheme("ace/theme/clouds");

        window.addEventListener('resize', function() {
            editor.resize();
        });

editor.setValue("select ");