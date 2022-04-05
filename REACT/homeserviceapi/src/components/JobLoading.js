import React from 'react';

function JobLoading(Component) {
    return function JobLoadingComponent({ isLoading, ...props}) {
        if (!isLoading) return <Component {...props} />;
        return (
            <p style={{ fontSize: '25px' }}>
                Waiting for data to load!...
            </p>
        );
    };
}

export default JobLoading;