document.addEventListener('htmx:afterRequest', function (event) {
    // check if request was triggered by the form inside the modal
    if (event.detail.requestConfig.path === '/crt-connection') {
        // check if request was successful
        if (event.detail.successful) {
            const modal = document.getElementById('connectionsModal');
            const closeButton = modal.querySelector('[data-modal-toggle="connectionsModal"]');

            if (closeButton) {
                closeButton.click();
            }

            // reload the page after 500ms (give it time to proc form)
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    }
});


function openEditModal(id, name, type, host, port, password, ssl, description, sid, svc_name, dsn, driver) {
    // console.log("openEditModal called with:", { id, name, type, host, port, password, ssl, description, sid, svc_name, dsn, driver });

    document.getElementById('editConnectionId').value = id;
    document.getElementById('editName').value = name || '';
    document.getElementById('editType').value = type || '';
    document.getElementById('editHost').value = host || '';
    document.getElementById('editPort').value = port || '';
    document.getElementById('editPassword').value = password || '';
    document.getElementById('editSsl').checked = ssl === 'true';
    document.getElementById('editDescription').value = description || '';
    document.getElementById('editSid').value = sid || '';
    document.getElementById('editSvcName').value = svc_name || '';
    document.getElementById('editDsn').value = dsn || '';
    document.getElementById('editDriver').value = driver || '';

    const modalToggleButton = document.querySelector('[data-modal-toggle="editConnectionModal"]');
    if (modalToggleButton) {
        modalToggleButton.click(); 
    }
}



document.addEventListener('htmx:afterRequest', function (event) {
    // check if request was triggered by the form inside the modal
    if (event.detail.requestConfig.path === '/update-connection') {
        // check if request was successful
        if (event.detail.successful) {
            const modal = document.getElementById('editConnectionModal');
            const closeButton = modal.querySelector('[data-modal-toggle="editConnectionsModal"]');

            if (closeButton) {
                closeButton.click();
            }

            // reload the page after 500ms (give it time to proc form)
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    }
});