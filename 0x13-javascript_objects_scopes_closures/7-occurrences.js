#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentelement) => currentelement === searchElement ? count + 1 : count, 0);
};
