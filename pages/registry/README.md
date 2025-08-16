# contextus.sh Website Pages

This directory contains the Jekyll website for contextus.sh.

## Development

The contextus.sh website is built using Jekyll. The easiest way to run the development server locally is using Docker, which avoids having to install Ruby and all dependencies on your machine.

### Using Docker (Recommended)

```bash
# Build and run the Jekyll site
docker run --rm -it \
  -v $(pwd):/srv/jekyll \
  -p 4000:4000 \
  jekyll/jekyll:latest \
  jekyll serve --host 0.0.0.0 --livereload
```

Then visit http://localhost:4000 to see the site.

### Local Ruby Installation

If you prefer to install Ruby and Jekyll locally:

```bash
# Install dependencies
bundle install

# Serve the site
bundle exec jekyll serve --livereload
```

## Structure

- `index.html` - Main landing page
- `registry/` - Registry browser page
- `_includes/` - Shared components (nav, footer, etc.)
- `_layouts/` - Page layouts
- `assets/` - CSS, JS, images
