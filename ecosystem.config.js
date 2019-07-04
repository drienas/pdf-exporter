module.exports = {
  apps: [
    {
      name: 'multiexporter: main',
      script: 'index.py',
      listen_timeout: 20000,
      env: {
        NODE_ENV: 'production'
      }
    }
  ]
};
