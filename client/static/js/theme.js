var themePreference = "ace/theme/clouds";

function changeTheme(theme) {
    editor.setTheme(theme);
    themePreference = theme;
    console.log(themePreference);
}