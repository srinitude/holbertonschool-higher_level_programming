#!/usr/bin/node
exports.callMeMoby = (reps, fn) => {
  for (let i = 0; i < reps; i++) {
    fn();
  }
};
