// default theme to match flowbite white
// users can then change theme using theme btn
var themePreference = "ace/theme/clouds";

function changeTheme(theme) {
    editor.setTheme(theme);
    themePreference = theme;
    console.log(themePreference);
}