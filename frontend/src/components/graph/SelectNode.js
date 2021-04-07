import React from "react";
import Select from "react-select";

const SelectNode = (props) => {
  const { nodes, setNodeStart, setNodeDestination } = props;

  const options = nodes.map((node, index) => {
    return {
      label: node.name,
      value: index,
    };
  });

  return (
    <>
      <div>
        <h3 className="mb-4 text-center select-node-title">Select Node</h3>
        <div className="mb-4">
          <h5>Node Start</h5>
          <Select
            options={options}
            onChange={(selected) => setNodeStart(selected.label)}
          />
        </div>
        <div className="mb-4">
          <h5>Node Destination</h5>
          <Select
            options={options}
            onChange={(selected) => setNodeDestination(selected.label)}
          />
        </div>
      </div>
      <style>
        {`
            .select-node-title {
                background: #B98389;
                color: #E4DBD9;
                padding: .5rem 1rem;
                border-radius: 7px; 
            }
        `}
      </style>
    </>
  );
};

export default SelectNode;
