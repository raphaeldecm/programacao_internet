// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
});

overlay.addEventListener('click', () => {
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
});

// Handle logout
function handleLogout() {
    if (confirm('Tem certeza que deseja sair?')) {
        // Redirect to logout URL
        window.location.href = '/logout/';
    }
}

// Simple chart rendering with Canvas
function drawSalesChart() {
    const canvas = document.getElementById('salesCanvas');
    if (!canvas) return;
    
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = 250;
    
    const ctx = canvas.getContext('2d');
    const data = [30, 45, 38, 52, 48, 65, 58, 72, 68, 78, 85, 92];
    const months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
    
    const padding = 40;
    const chartWidth = canvas.width - padding * 2;
    const chartHeight = canvas.height - padding * 2;
    const max = Math.max(...data);
    const barWidth = chartWidth / data.length;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw bars
    data.forEach((value, index) => {
        const barHeight = (value / max) * chartHeight;
        const x = padding + index * barWidth + barWidth * 0.2;
        const y = canvas.height - padding - barHeight;
        const width = barWidth * 0.6;
        
        // Gradient
        const gradient = ctx.createLinearGradient(0, y, 0, canvas.height - padding);
        gradient.addColorStop(0, '#6366f1');
        gradient.addColorStop(1, '#8b5cf6');
        
        ctx.fillStyle = gradient;
        ctx.fillRect(x, y, width, barHeight);
        
        // Month labels
        ctx.fillStyle = '#64748b';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(months[index], x + width / 2, canvas.height - 15);
    });
}

function drawProductsChart() {
    const canvas = document.getElementById('productsCanvas');
    if (!canvas) return;
    
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = 250;
    
    const ctx = canvas.getContext('2d');
    const data = [
        { name: 'Produto A', value: 35, color: '#6366f1' },
        { name: 'Produto B', value: 25, color: '#8b5cf6' },
        { name: 'Produto C', value: 20, color: '#10b981' },
        { name: 'Produto D', value: 12, color: '#f59e0b' },
        { name: 'Produto E', value: 8, color: '#ef4444' }
    ];
    
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) - 40;
    
    let currentAngle = -Math.PI / 2;
    const total = data.reduce((sum, item) => sum + item.value, 0);
    
    // Draw pie slices
    data.forEach((item, index) => {
        const sliceAngle = (item.value / total) * Math.PI * 2;
        
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
        ctx.closePath();
        ctx.fillStyle = item.color;
        ctx.fill();
        
        currentAngle += sliceAngle;
    });
    
    // Draw legend
    let legendY = 20;
    data.forEach((item, index) => {
        ctx.fillStyle = item.color;
        ctx.fillRect(20, legendY, 12, 12);
        
        ctx.fillStyle = '#1e293b';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(`${item.name} (${item.value}%)`, 38, legendY + 10);
        
        legendY += 25;
    });
}

// Initialize charts on page load
window.addEventListener('load', () => {
    drawSalesChart();
    drawProductsChart();
});

// Redraw charts on window resize
window.addEventListener('resize', () => {
    drawSalesChart();
    drawProductsChart();
});

// Simulate real-time updates (optional)
function updateStats() {
    // This function could be used to fetch and update stats periodically
    // Example: fetch('/api/stats/').then(data => { ... })
}

// Active navigation highlight
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        e.currentTarget.classList.add('active');
    });
});