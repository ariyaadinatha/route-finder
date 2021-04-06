import React from "react";

const AdjacencyMatrix = (props) => {
  const { adjMatrix, handleToggleElement } = props;

  return (
    <>
      {/* {console.log(adjMatrix)} */}
      <div className="adj-title-container d-flex text-center">
        <h3 className="adj-title w-100">Adjacency Matrix</h3>
      </div>
      {adjMatrix.map((row, i) => {
        return (
          <div className="matrix-row d-flex" key={i}>
            {row.map((el, j) => {
              return (
                <div className={`m-1`}>
                  <button
                    onClick={() => handleToggleElement(i, j)}
                    key={j}
                    className={`adj-element adj-element-${
                      el === 0 ? "0" : "1"
                    }`}
                  >
                    {el}
                  </button>
                </div>
              );
            })}
          </div>
        );
      })}
      <style>
        {`
            .adj-title {
                background: #B98389;
                color: #E4DBD9;
                padding: .5rem 0rem;
                border-radius: 7px;                
            }

            .adj-element {
                border: none;
                outline: none;
                padding: .2rem .5rem;
                border-radius: 4px;
            }

            .adj-element:focus {
                border: none;
                outline: none;
            }

            .adj-element-0 {
                background: #e4dbd9;
                color: #111b1e;
            }

            .adj-element-1 {
                background: #2F4C58;
                color: #e4dbd9;
            }
        `}
      </style>
    </>
  );
};

export default AdjacencyMatrix;
