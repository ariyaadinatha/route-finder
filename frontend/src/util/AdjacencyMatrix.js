export const addNodeToMatrix = (matrix) => {
  const matrixSize = matrix.length;

  var newMatrix = [];
  var i, j;

  for (i = 0; i < matrixSize + 1; i++) {
    var newRow = [];
    for (j = 0; j < matrixSize + 1; j++) {
      if (i === matrixSize || j === matrixSize) {
        newRow[j] = 0;
      } else {
        newRow[j] = matrix[i][j];
      }
    }
    newMatrix[i] = newRow;
  }
  return newMatrix;
};

export const addVertexToMatrix = (matrix, i, j) => {
  const newElement = matrix[i][j] === 0 ? 1 : 0;
  var newMatrix = [...matrix];

  newMatrix[i][j] = newElement;
  newMatrix[j][i] = newElement;

  return newMatrix;
};

export const deleteNodeFromMatrix = (matrix, index) => {
  var newMatrix = [];

  matrix.forEach((row, i) => {
    var newRow = [];
    row.forEach((el, j) => {
      if (i !== index && j !== index) {
        newRow = newRow.concat(el);
      }
    });

    if (newRow.length > 0) {
      newMatrix = newMatrix.concat([newRow]);
    }
  });

  return newMatrix;
};
