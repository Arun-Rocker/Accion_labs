# Use minimal Alpine-based image with fixed version
FROM nginx:1.19-alpine

# Remove default configs to reduce attack surface
RUN rm -rf /etc/nginx/conf.d/default.conf

# Copy custom hardened configuration
COPY nginx.conf /etc/nginx/conf.d/

# Set non-root permissions
RUN chown -R nginx:nginx /var/cache/nginx && \
    chmod -R 755 /var/log/nginx

# Run as non-root user, this will reduce the risk
USER nginx

# Expose only necessary port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]