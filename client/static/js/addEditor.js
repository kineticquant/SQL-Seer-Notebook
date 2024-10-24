document.getElementById('addEditor').addEventListener('click', () => {
    // get the number of editors, increment for unique ID
    const editorCount = document.querySelectorAll('.editor-instance').length + 1;

    // create  a container div for the new editor and the buttons
    const editorContainer = document.createElement('div');
    editorContainer.classList.add('mt-4', 'mb-4', 'max-w-screen-xl', 'mx-auto');

    // create a new editor div with a unique ID
    const editorDiv = document.createElement('div');
    editorDiv.id = `editor${editorCount}`;
    editorDiv.classList.add('editor-instance', 'resize-y', 'h-48', 'border', 'border-gray-300', 'rounded', 'max-w-screen-xl', 'mx-auto');
    editorDiv.style.height = '300px';

    const buttonBar = document.createElement('div');
    buttonBar.classList.add('flex', 'space-x-1');
    buttonBar.innerHTML = `
        <button id="runQuery${editorCount}" class="mt-5 mb-1 bg-blue-500 border border-black text-white px-4 rounded text-sm">Run</button>
        <button id="clearEditor${editorCount}" class="mt-5 mb-1 border border-black text-black px-4 rounded text-sm bg-transparent hover:bg-black hover:text-white">Clear</button>
        <select id="connectionSelector" class="mt-5 mb-1 border border-black bg-transparent text-black px-1 rounded text-sm">
            <option value="option1">Test SQLLite DB - PHX</option>
            <option value="option2">Option 2</option>
            <option value="option3">Option 3</option>
        </select>
    `;

    // append new editor and buttons to the container div
    editorContainer.appendChild(buttonBar);
    editorContainer.appendChild(editorDiv);

    // append entire container to the body or a specific section
    document.body.appendChild(editorContainer);

    // initialize editor for the new editor div
    const dynamicEditorWin = ace.edit(`editor${editorCount}`);
    dynamicEditorWin.session.setMode("ace/mode/sql");
    dynamicEditorWin.setTheme("ace/theme/clouds");

    // add functionality for the new Run button
    document.getElementById(`runQuery${editorCount}`).addEventListener('click', () => {
        const query = dynamicEditorWin.getValue();
        // Handle the query logic for the new editor
        console.log(`Running query from editor${editorCount}:`, query);
    });

    // add functionality for the new Clear button
    document.getElementById(`clearEditor${editorCount}`).addEventListener('click', () => {
        dynamicEditorWin.setValue('', '');
    });

    // resize where applicable
    editorDiv.addEventListener('mousemove', () => {
        dynamicEditorWin.resize();
    });
});
