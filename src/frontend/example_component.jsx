import React from "react";

function StepDisplay({ step, guidance }) {
    return (
        <div>
            <h3>Step: {step}</h3>
            <p>{guidance}</p>
        </div>
    );
}

export default StepDisplay;
