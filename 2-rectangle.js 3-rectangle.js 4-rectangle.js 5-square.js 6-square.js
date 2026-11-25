[1mdiff --git a/javascript_objects_scopes_closures/1-rectangle.js b/javascript_objects_scopes_closures/1-rectangle.js[m
[1mindex 5dfd0b5..ec7274a 100755[m
[1m--- a/javascript_objects_scopes_closures/1-rectangle.js[m
[1m+++ b/javascript_objects_scopes_closures/1-rectangle.js[m
[36m@@ -1,6 +1,6 @@[m
 #!/usr/bin/node[m
 class Rectangle {[m
[31m-  constructor(w, h) {[m
[32m+[m[32m  constructor (w, h) {[m
     this.width = w;[m
     this.height = h;[m
   }[m
[1mdiff --git a/javascript_objects_scopes_closures/2-rectangle.js b/javascript_objects_scopes_closures/2-rectangle.js[m
[1mindex 0012357..c9c99c7 100755[m
[1m--- a/javascript_objects_scopes_closures/2-rectangle.js[m
[1m+++ b/javascript_objects_scopes_closures/2-rectangle.js[m
[36m@@ -1,6 +1,6 @@[m
 #!/usr/bin/node[m
 class Rectangle {[m
[31m-  constructor(w, h) {[m
[32m+[m[32m  constructor (w, h) {[m
     if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {[m
       this.width = w;[m
       this.height = h;[m
[1mdiff --git a/javascript_objects_scopes_closures/3-rectangle.js b/javascript_objects_scopes_closures/3-rectangle.js[m
[1mindex 0baacfa..a764b0f 100755[m
[1m--- a/javascript_objects_scopes_closures/3-rectangle.js[m
[1m+++ b/javascript_objects_scopes_closures/3-rectangle.js[m
[36m@@ -1,13 +1,13 @@[m
 #!/usr/bin/node[m
 class Rectangle {[m
[31m-  constructor(w, h) {[m
[32m+[m[32m  constructor (w, h) {[m
     if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {[m
       this.width = w;[m
       this.height = h;[m
     }[m
   }[m
 [m
[31m-  print() {[m
[32m+[m[32m  print () {[m
     for (let i = 0; i < this.height; i++) {[m
       console.log('X'.repeat(this.width));[m
     }[m
[1mdiff --git a/javascript_objects_scopes_closures/4-rectangle.js b/javascript_objects_scopes_closures/4-rectangle.js[m
[1mindex 4c02435..138ed12 100755[m
[1m--- a/javascript_objects_scopes_closures/4-rectangle.js[m
[1m+++ b/javascript_objects_scopes_closures/4-rectangle.js[m
[36m@@ -1,25 +1,25 @@[m
 #!/usr/bin/node[m
 class Rectangle {[m
[31m-  constructor(w, h) {[m
[32m+[m[32m  constructor (w, h) {[m
     if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {[m
       this.width = w;[m
       this.height = h;[m
     }[m
   }[m
 [m
[31m-  print() {[m
[32m+[m[32m  print () {[m
     for (let i = 0; i < this.height; i++) {[m
       console.log('X'.repeat(this.width));[m
     }[m
   }[m
 [m
[31m-  rotate() {[m
[32m+[m[32m  rotate () {[m
     const temp = this.width;[m
     this.width = this.height;[m
     this.height = temp;[m
   }[m
 [m
[31m-  double() {[m
[32m+[m[32m  double () {[m
     this.width *= 2;[m
     this.height *= 2;[m
   }[m
[1mdiff --git a/javascript_objects_scopes_closures/5-square.js b/javascript_objects_scopes_closures/5-square.js[m
[1mindex 86efdb0..c56eb89 100755[m
[1m--- a/javascript_objects_scopes_closures/5-square.js[m
[1m+++ b/javascript_objects_scopes_closures/5-square.js[m
[36m@@ -2,7 +2,7 @@[m
 const Rectangle = require('./4-rectangle');[m
 [m
 class Square extends Rectangle {[m
[31m-  constructor(size) {[m
[32m+[m[32m  constructor (size) {[m
     super(size, size);[m
   }[m
 }[m
[1mdiff --git a/javascript_objects_scopes_closures/6-square.js b/javascript_objects_scopes_closures/6-square.js[m
[1mindex 2e48cfa..cb8a4a1 100755[m
[1m--- a/javascript_objects_scopes_closures/6-square.js[m
[1m+++ b/javascript_objects_scopes_closures/6-square.js[m
[36m@@ -2,7 +2,7 @@[m
 const Square = require('./5-square');[m
 [m
 class NewSquare extends Square {[m
[31m-  charPrint(c) {[m
[32m+[m[32m  charPrint (c) {[m
     const char = c === undefined ? 'X' : c;[m
     for (let i = 0; i < this.height; i++) {[m
       console.log(char.repeat(this.width));[m
