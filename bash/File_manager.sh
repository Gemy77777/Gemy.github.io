#!/usr/bin/env bash

TARGET_DIR="${1:-.}"

echo "Organizing files in $TARGET_DIR"
mkdir -p "$TARGET_DIR/images"
mkdir -p "$TARGET_DIR/docs"
mkdir -p "$TARGET_DIR/videos"
mkdir -p "$TARGET_DIR/others"
mkdir -p "$TARGET_DIR/music"

echo "Moving images..."
mv "$TARGET_DIR"/*.jpg "$TARGET_DIR/images/" 2>/dev/null
mv "$TARGET_DIR"/*.jpeg "$TARGET_DIR/images/" 2>/dev/null
mv "$TARGET_DIR"/*.png "$TARGET_DIR/images/" 2>/dev/null
mv "$TARGET_DIR"/*.gif "$TARGET_DIR/images/" 2>/dev/null

echo "Moving documents..."
mv "$TARGET_DIR"/*.pdf "$TARGET_DIR/docs/" 2>/dev/null
mv "$TARGET_DIR"/*.doc "$TARGET_DIR/docs/" 2>/dev/null
mv "$TARGET_DIR"/*.docx "$TARGET_DIR/docs/" 2>/dev/null
mv "$TARGET_DIR"/*.txt "$TARGET_DIR/docs/" 2>/dev/null

echo "Moving videos..."
mv "$TARGET_DIR"/*.mp4 "$TARGET_DIR/videos/" 2>/dev/null
mv "$TARGET_DIR"/*.avi "$TARGET_DIR/videos/" 2>/dev/null
mv "$TARGET_DIR"/*.mkv "$TARGET_DIR/videos/" 2>/dev/null

echo "Moving music..."
mv "$TARGET_DIR"/*.mp3 "$TARGET_DIR/music/" 2>/dev/null
mv "$TARGET_DIR"/*.wav "$TARGET_DIR/music/" 2>/dev/null

echo "Moving other files..."
mv "$TARGET_DIR"/*.* "$TARGET_DIR/others/" 2>/dev/null


echo "===================================="
echo "Organizing complete!"
echo "Files organized in: $TARGET_DIR"
echo "Folders created: images, docs, videos, others"
echo "===================================="



