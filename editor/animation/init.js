//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function netGameCanvas(dom, inp, out, data) {

            const ANIMATION_THRESHOLD = 1000
            const os = 10
            const [w, h] = [inp[0].length, inp.length]
            const big = (w*h >= ANIMATION_THRESHOLD)
            const size = 300 / Math.max(w, h)
            const paper = Raphael(dom, size*w+(os*2), size*h+(os*2), 0, 0)
            const dic = {N: 'E', E: 'S', S: 'W', W: 'N'}

            /*----------------------------------------*
             *
             * anmation
             *
             *----------------------------------------*/
            let idx = -1 
            const fn2 = function () {

                idx += 1
                const tl = tiles[idx]

                if (idx >= tiles.length) {
                    return
                }

                const deg = get_rotate_degree(
                    inp[tl.r][tl.c], out[tl.r][tl.c])

                tl.obj.animate(
                    {'fill': '#8EC6EC'},
                    600, 
                )
                tl.obj.animate(
                    {transform: 'r' + (deg) + ','+(tl.x)+','+(tl.y)},
                    50*Math.max(1, 75/(w*h)), 
                    '<>',
                    fn2
                )
            }

            /*----------------------------------------*
             *
             * draw tile
             *
             *----------------------------------------*/
            function draw_tile(x, y, r, c) {
                const t = paper.set()
                const dirs = (big ? out[r][c]: inp[r][c])
                const attr_rect = (big ?
                    attr.rect.out:
                    attr.rect.in)
                const attr_terminal = (big ?
                    attr.terminal.out:
                    attr.terminal.in)

                t.push(paper.rect(x, y, size, size).attr(attr_rect))

                if (dirs.indexOf('N') > -1) {
                    t.push(paper.path('M' + (x+(size/2)) + ',' 
                        + (y+(size/2))
                        + ' l' + (0) + ',' + (-1*size/2)).attr(
                            attr.line.connection))
                }

                if (dirs.indexOf('E') > -1) {
                    t.push(paper.path('M' + (x+(size/2)) + ',' 
                        + (y+(size/2))
                        + ' l' + (size/2) + ',' + (0)).attr(
                            attr.line.connection))
                }

                if (dirs.indexOf('W') > -1) {
                    t.push(paper.path('M' + (x+(size/2)) + ',' 
                        + (y+(size/2))
                        + ' l' + (-1*(size/2)) + ',' + (0)).attr(
                            attr.line.connection))
                }

                if (dirs.indexOf('S') > -1) {
                    t.push(paper.path('M' + (x+(size/2)) + ',' 
                        + (y+(size/2))
                        + ' l' + (0) + ',' + (size/2)).attr(
                            attr.line.connection))
                }

                // terminal
                if (dirs.length === 1) {
                    const tm_size = size/4
                    const tm_os = (size - tm_size)/2
                    t.push(
                        paper.rect(
                            x+tm_os, y+tm_os, tm_size, tm_size).attr(
                            attr_terminal))
                }
                return t;

            }

            /*----------------------------------------*
             *
             * get rotate degree
             *
             *----------------------------------------*/
            function get_rotate_degree(it, ot) {
                let degree = 0
                it = it.split('').sort()
                ot = ot.split('').sort()

                let i = 0
                while (i < 4) {
                    if (it.toString() == ot.toString()) {
                        break
                    }
                    it = it.map(ch=>dic[ch]).sort()
                    degree += 90
                    i += 1

                }
                return degree > 180 ? degree - 360: degree
            }

            // main

            const attr = {
                rect: {
                    in: {
                        'stroke': '#8EC6EC',
                        'stroke-width': 0.2,
                        'fill': 'white',
                    },
                    out: {
                        'stroke': '#8EC6EC',
                        'stroke-width': 0.2,
                        'fill': '#8EC6EC',
                    },
                },
                terminal: {
                    in: {
                        'stroke': '#163E69',
                        'stroke-width': 0.5,
                        'fill': '#006CA9',
                    },
                    out: {
                        'stroke': '#163E69',
                        'stroke-width': 0.5,
                        'fill': '#8EC6EC',
                    },
                },
                line: {
                    connection: {
                        'stroke': '#163E69',
                        'fill': '#163E69',
                        'stroke-width': 0.5,
                    },
                },
            }

            // set canvas
            if (! out) {
                return
            }

            // draw grid
            const tiles = []
            for (let r=0; r < h; r += 1) {
                for (let c=0; c < w; c += 1) {
                    tiles.push({
                        obj: draw_tile(c*size+os, r*size+os, r, c),
                        r: r,
                        c: c,
                        x: c*size+os+size/2,
                        y: r*size+os+size/2,
                    })
                }
            }

            // Task solved ?
            if (! data.ext.result) {
                return
            }

            // do animation ?
            if (! big) {
                fn2()
            }
        }

        /*----------------------------------------*
         *
         *----------------------------------------*/
        var $tryit;

        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'checkio',
                js: 'checkio'
            },
            animation: function($expl, data){
                netGameCanvas(
                    $expl[0],
                    data.in,
                    data.out,
                    data,
                );
            }
        });
        io.start();
    }
);
