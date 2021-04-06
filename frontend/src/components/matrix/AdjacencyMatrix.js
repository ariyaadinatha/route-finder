import React from "react";

const AdjacencyMatrix = (props) => {
  const { adjMatrix, handleToggleElement } = props;

  return (
    <>
      {/* {console.log(adjMatrix)} */}
      <p>Adjacency Matrix</p>
      {adjMatrix.map((row, i) => {
        return (
          <div className="matrix-row" key={i}>
            {row.map((el, j) => {
              return (
                <button onClick={() => handleToggleElement(i, j)} key={j}>
                  {el}
                </button>
              );
            })}
          </div>
        );
      })}
      <style>
        {`
            .matrix-row {
                display: flex
            }
        `}
      </style>
    </>
  );
};

export default AdjacencyMatrix;
