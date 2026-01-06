function copyToClipboard(elementId, btn) {
    const text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = btn.innerHTML;
        btn.classList.add('copied');
        btn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            Copiado!
        `;
        
        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = originalText;
        }, 2000);
    });
}

function toggleFavorito(pk, btn) {
    const url = document.getElementById('toggle-favorito-url').dataset.url.replace('0', pk);
    
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.favorito) {
            btn.classList.add('active');
            btn.title = 'Remover dos favoritos';
        } else {
            btn.classList.remove('active');
            btn.title = 'Adicionar aos favoritos';
        }
        location.reload();
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function abrirModalAdicao() {
    document.getElementById('modalAdicao').style.display = 'flex';
}

function fecharModalAdicao() {
    document.getElementById('modalAdicao').style.display = 'none';
}

function abrirModalEdicao(pk, titulo, conteudo) {
    const modal = document.getElementById('modalEdicao');
    const form = document.getElementById('formEdicao');
    const url = document.getElementById('editar-colinha-url').dataset.url.replace('0', pk);
    
    document.getElementById('editTitulo').value = titulo;
    document.getElementById('editConteudo').value = conteudo;
    form.action = url;
    
    modal.style.display = 'flex';
}

function fecharModalEdicao() {
    document.getElementById('modalEdicao').style.display = 'none';
}

function abrirModalExclusao(pk, titulo) {
    const modal = document.getElementById('modalExclusao');
    const form = document.getElementById('formExclusao');
    const url = document.getElementById('excluir-colinha-url').dataset.url.replace('0', pk);
    
    document.getElementById('tituloExclusao').innerText = titulo;
    form.action = url;
    
    modal.style.display = 'flex';
}

function fecharModalExclusao() {
    document.getElementById('modalExclusao').style.display = 'none';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Drag and Drop - Lógica de Proximidade Euclidiana para Grids
let draggedElement = null;
let draggedGrid = null;
let placeholder = null;

function createPlaceholder() {
    const div = document.createElement('div');
    div.className = 'colinha-card drag-placeholder';
    div.style.border = '2px dashed var(--primary-color)';
    div.style.background = 'rgba(0, 69, 196, 0.05)';
    div.style.minHeight = '150px';
    div.style.pointerEvents = 'none';
    return div;
}

function initDragAndDrop() {
    const cards = document.querySelectorAll('.draggable-card');
    const grids = document.querySelectorAll('.sortable-grid');

    cards.forEach(card => {
        card.addEventListener('dragstart', handleDragStart);
        card.addEventListener('dragend', handleDragEnd);
    });

    grids.forEach(grid => {
        grid.addEventListener('dragover', handleDragOver);
        grid.addEventListener('drop', handleDrop);
    });
}

function handleDragStart(e) {
    draggedElement = this;
    draggedGrid = this.closest('.sortable-grid');
    this.classList.add('dragging');
    placeholder = createPlaceholder();
    e.dataTransfer.setData('text/plain', '');
    e.dataTransfer.effectAllowed = 'move';
}

function handleDragEnd(e) {
    this.classList.remove('dragging');
    if (placeholder && placeholder.parentNode) {
        placeholder.parentNode.removeChild(placeholder);
    }
    draggedElement = null;
    draggedGrid = null;
    placeholder = null;
}

function handleDragOver(e) {
    e.preventDefault();
    if (!draggedElement || draggedGrid !== this) return;
    
    const afterElement = getDragAfterElement(this, e.clientX, e.clientY);
    
    if (afterElement == null) {
        this.appendChild(placeholder);
    } else {
        this.insertBefore(placeholder, afterElement);
    }
}

function handleDrop(e) {
    e.preventDefault();
    if (!draggedElement || draggedGrid !== this) return;
    
    if (placeholder && placeholder.parentNode) {
        placeholder.parentNode.insertBefore(draggedElement, placeholder);
        placeholder.parentNode.removeChild(placeholder);
    }
    
    salvarOrdem(this);
}

/**
 * Determina a posição correta no grid considerando o fluxo natural (esquerda->direita, cima->baixo)
 */
function getDragAfterElement(container, x, y) {
    const draggableElements = [...container.querySelectorAll('.draggable-card:not(.dragging):not(.drag-placeholder)')];
    
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        
        // Calcula o ponto central do card
        const centerX = box.left + box.width / 2;
        const centerY = box.top + box.height / 2;
        
        // Mouse está acima do card? Inserir antes
        if (y < box.top) {
            return closest || child;
        }
        
        // Mouse está na mesma linha (aproximadamente)?
        const isInSameRow = y >= box.top && y <= box.bottom;
        
        if (isInSameRow) {
            // Se mouse está à esquerda do centro, inserir antes deste card
            if (x < centerX) {
                return child;
            }
        } else if (y > box.bottom) {
            // Mouse está abaixo, continue procurando
            return null;
        }
        
        return closest;
    }, null);
}

function salvarOrdem(grid) {
    const cards = grid.querySelectorAll('.draggable-card');
    const ordem = Array.from(cards).map(card => card.dataset.id);
    const urlElement = document.getElementById('reordenar-colinhas-url');
    if (!urlElement) return;
    
    fetch(urlElement.dataset.url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ordem: ordem })
    })
    .then(response => response.json())
    .catch(error => console.error('Erro ao salvar ordem:', error));
}

window.onclick = function(event) {
    const modalAdicao = document.getElementById('modalAdicao');
    const modalEdicao = document.getElementById('modalEdicao');
    const modalExclusao = document.getElementById('modalExclusao');
    
    if (event.target == modalAdicao) fecharModalAdicao();
    if (event.target == modalEdicao) fecharModalEdicao();
    if (event.target == modalExclusao) fecharModalExclusao();
}

document.addEventListener('DOMContentLoaded', function() {
    initDragAndDrop();
});
