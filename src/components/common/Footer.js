import React from 'react';

const Footer = () => {
    const thisYear = () => {
        const year = new Date().getFullYear();
        return year
    };

    return (
        <div id='footer' className='text-center p-2'>
            <p>
                HoleInOne
            </p>
            <p>
                에이콘아카데미 3조
            </p>
            <p>
                강민혁, 박소현, 박제현, 유국토, 정기용, 최민섭
            </p>
            <p>
                Copyright &copy; <span>{thisYear()}</span> All right reserved
            </p>
        </div>
    )
};

export default Footer;