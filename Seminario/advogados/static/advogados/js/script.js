// Função para excluir um advogado
function confirmarExclusao(id) {
    if (confirm('Tem certeza que deseja excluir este advogado?')) {
        fetch(`/advogados/excluir/${id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => {
            if (response.ok) {
                document.getElementById(`advogado_${id}`).remove();
            } else {
                alert('Erro ao excluir o advogado');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao excluir o advogado');
        });
    }
}

// Função para adicionar um advogado via AJAX
document.getElementById('formAdicionar')?.addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    let formData = new FormData(this);
    
    fetch('/advogados/adicionar/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json()) // Espera resposta JSON
    .then(data => {
        if (data.success) {
            let novoAdvogado = data.advogado;
            let table = document.getElementById('advogadosTable').getElementsByTagName('tbody')[0];
            let newRow = table.insertRow();
            newRow.id = `advogado_${novoAdvogado.id}`;
            newRow.innerHTML = `
                <td>${novoAdvogado.nome}</td>
                <td>${novoAdvogado.email}</td>
                <td>${novoAdvogado.telefone}</td>
                <td>${novoAdvogado.OAB}</td>
                <td>
                    <a href="/advogados/editar/${novoAdvogado.id}/">Editar</a>
                    <a href="javascript:void(0);" onclick="confirmarExclusao(${novoAdvogado.id})">Excluir</a>
                </td>
            `;
        } else {
            alert('Erro ao adicionar o advogado');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao adicionar o advogado');
    });
});

// Função para editar um advogado via AJAX
document.getElementById('formEditar')?.addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    let formData = new FormData(this);
    let id = document.getElementById('advogadoId').value; // Supondo que o ID do advogado esteja no campo hidden

    fetch(`/advogados/editar/${id}/`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json()) // Espera resposta JSON
    .then(data => {
        if (data.success) {
            // Atualiza a linha da tabela com os novos dados
            let row = document.getElementById(`advogado_${data.advogado.id}`);
            row.cells[0].textContent = data.advogado.nome;
            row.cells[1].textContent = data.advogado.email;
            row.cells[2].textContent = data.advogado.telefone;
            row.cells[3].textContent = data.advogado.OAB;
        } else {
            alert('Erro ao editar o advogado');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao editar o advogado');
    });
});
